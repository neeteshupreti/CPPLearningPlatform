# learning/utils.py
from .models import Badge, UserAchievement

def award_badge(user, badge_name):
    """Award badge to user if not already earned"""
    badge = Badge.objects.filter(name=badge_name).first()
    profile = user.learning_profile

    if badge and badge not in profile.badges.all():
        profile.badges.add(badge)
        profile.save()
        # Save achievement history
        UserAchievement.objects.create(user=user, badge=badge)
        return True
    return False
