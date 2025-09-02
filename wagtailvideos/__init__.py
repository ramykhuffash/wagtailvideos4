from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

default_app_config = 'wagtailvideos.apps.WagtailVideosApp'

# Cache the model once it's loaded
_video_model = None


def is_modeladmin_installed():
    from django.apps import apps
    return apps.is_installed('wagtail.contrib.modeladmin')


def get_video_model_string():
    return getattr(settings, 'WAGTAILVIDEOS_VIDEO_MODEL', 'wagtailvideos.Video')


def get_video_model():
    global _video_model
    
    # Return cached model if already loaded
    if _video_model is not None:
        return _video_model
    
    from django.apps import apps
    
    # Try to get the model, but don't fail during Django startup
    model_string = get_video_model_string()
    try:
        _video_model = apps.get_model(model_string)
        return _video_model
    except ValueError:
        raise ImproperlyConfigured("WAGTAILVIDEOS_VIDEO_MODEL must be of the form 'app_label.model_name'")
    except LookupError as e:
        # During Django startup, models might not be available yet
        # Check if it's a startup issue vs a real config problem
        if apps.ready:
            # Apps are ready but model still not found - real error
            raise ImproperlyConfigured(
                "WAGTAILVIDEOS_VIDEO_MODEL refers to model '%s' that has not been installed" % model_string
            )
        else:
            # Apps not ready yet, try to import the model class directly as fallback
            try:
                from django.utils.module_loading import import_string
                app_label, model_name = model_string.split('.')
                model_class_path = f"{app_label}.models.{model_name}"
                _video_model = import_string(model_class_path)
                return _video_model
            except:
                # If that fails too, return None and let it be resolved later
                return None