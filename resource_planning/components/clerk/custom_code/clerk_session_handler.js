function ClerkSessionHandler({ children }) {
    /* To get the token and add an event to store the token in the state */

    const { getToken, isLoaded, isSignedIn } = useAuth()
    const { user } = useUser()
    const [addEvents, connectErrors] = useContext(EventLoopContext)

    useEffect(() => {
        if (isLoaded && !!addEvents) {
            if (isSignedIn) {
                getToken().then(token => {
                    addEvents([Event("%s.set_clerk_session", { token, user })])
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