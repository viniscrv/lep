from django.urls import path
from .views import ReportActivities

app_name = "reports"

urlpatterns = [
    path(
        "most_performed_activity/",
        ReportActivities.as_view({"get": "get_most_performed_activity"}),
        name="most_performed_activity"
    ),
    path(
        "best_streak/",
        ReportActivities.as_view({"get": "get_best_streak"}),
        name="best_streak"
    ),
]