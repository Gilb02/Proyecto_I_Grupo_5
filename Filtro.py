import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject

Gst.init(None)

pipeline = Gst.parse_launch("v4l2src ! videoconvert ! edgetv ! videoconvert ! ximagesink")

pipeline.set_state(Gst.State.PLAYING)

bus = pipeline.get_bus()
msg = bus.timed_pop_filtered(Gst.CLOCK_TIME_NONE, Gst.MessageType.EOS)

pipeline.set_state(Gst.State.NULL)

