from django.contrib import admin
from django.urls import include, path

from plandiet_app.views import Index, MacroCalculatorView

urlpatterns = [
    path("", include("categories.urls")),
    path("", include("diets.urls")),
    path("", include("exercises.urls")),
    path("", include("plans.urls")),
    path("", include("users.urls")),
    path("admin/", admin.site.urls),
    path("", Index.as_view(), name="index"),
    path("macro_calculator/", MacroCalculatorView.as_view(), name="macro-calc"),
]

urlpatterns += [path("silk/", include("silk.urls", namespace="silk"))]
urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]
