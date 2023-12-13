from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class AnonSustainedThrottle(AnonRateThrottle):
    scope = "anon_sustained"

class UserSustainedThrottle(UserRateThrottle):
    scope = "user_sustained"

class AnonBurstThrottle(AnonRateThrottle):
    scope = "anon_burst"

class UserBurstThrottle(UserRateThrottle):
    scope = "user_burst"