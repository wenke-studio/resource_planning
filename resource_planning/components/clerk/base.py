import reflex as rx

import os


class ClerkComponent(rx.Component):
    library: str = "@clerk/clerk-react"


class ClerkState(rx.State):
    is_signed_in: bool = False

    user_id: str = ""

    claims: str = ""

    user: str = ""

    def set_clerk_session(self, token: str):
        self.is_signed_in = True
        # todo: decode the jwt token than set user_id and claims
        self.user_id = 1

        # todo: trigger .fetch_user()
        if self.user_id:
            self.fetch_user()

    def clear_clerk_session(self):
        self.is_signed_in = False
        # todo: needs to dosomething
        pass

    def fetch_user(self):
        # todo: create clerk api than fill me
        self.user = "test"
        # if self.user_id:
        #     self.user = clerk.api.get_user(self.user_id)
        #     self.set_user(self.user)


class ClerkSession(rx.Component):
    tag: str = "ClerkSession"

    def add_imports(self) -> dict:
        return {
            "@clerk/clerk-react": ["useAuth"],
            "react": ["useContext", "useEffect"],
            "/utils/context": ["EventLoopContext"],
            "/utils/state": ["Event"],
        }

    def add_custom_code(self) -> list[str]:
        clerk_state_name = ClerkState.get_full_name()

        # todo: refactor me
        return [
            """
function ClerkSession({ children }) {
  const { getToken, isLoaded, isSignedIn } = useAuth()
  const [ addEvents, connectErrors ] = useContext(EventLoopContext)

  useEffect(() => {
      if (isLoaded && !!addEvents) {
        if (isSignedIn) {
          getToken().then(token => {
            addEvents([Event("%s.set_clerk_session", {token})])
          })
        } else {
          addEvents([Event("%s.clear_clerk_session")])
        }
      }
  }, [isSignedIn])      

  return (
      <>{children}</>
  )
}
"""
            % (clerk_state_name, clerk_state_name)
        ]


class ClerkProvider(ClerkComponent):
    tag: str = "ClerkProvider"

    publishable_key: str = os.getenv("CLERK_PUBLISHABLE_KEY")

    # @classmethod
    # def create(cls, *children, **props):
    #     session = ClerkSession.create(*children)
    #     provider = super().create(session, **props)
    #     return rx.fragment(provider)


clerk_provider = ClerkProvider.create
clerk_session = ClerkSession.create
