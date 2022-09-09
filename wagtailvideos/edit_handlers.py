from wagtail.admin.panels import FieldPanel

from .widgets import AdminVideoChooser


class VideoChooserPanel(FieldPanel):
    model = None
    field_name = None
    _target_model = None

    object_type_name = "video"

    def widget_overrides(self):
        return {self.field_name: AdminVideoChooser}
