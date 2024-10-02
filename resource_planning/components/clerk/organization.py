from .base import ClerkComponent


class CreateOrganization(ClerkComponent):
    tag: str = "CreateOrganization"


class OrganizationProfile(ClerkComponent):
    tag: str = "OrganizationProfile"


class OrganizationSwitcher(ClerkComponent):
    tag: str = "OrganizationSwitcher"


class OrganizationList(ClerkComponent):
    tag: str = "OrganizationList"


create_organization = CreateOrganization.create
organization_profile = OrganizationProfile.create
organization_switcher = OrganizationSwitcher.create
organization_list = OrganizationList.create
