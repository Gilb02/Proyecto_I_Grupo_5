import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject

Gst.init(None)

pipeline = Gst.Pipeline()
src = Gst.ElementFactory.make("v4l2src")
videoconvert1 = Gst.ElementFactory.make("videoconvert")
edge = Gst.ElementFactory.make("edgetv")
videoconvert2 = Gst.ElementFactory.make("videoconvert")
ximagesink = Gst.ElementFactory.make("ximagesink")

pipeline.add(src)
pipeline.add(videoconvert1)
pipeline.add(edge)
pipeline.add(videoconvert2)
pipeline.add(ximagesink)

src.link(videoconvert1)
videoconvert1.link(edge)
edge.link(videoconvert2)
videoconvert2.link(ximagesink)

pipeline.set_state(Gst.State.PLAYING)

bus = pipeline.get_bus()
msg = bus.timed_pop_filtered(Gst.CLOCK_TIME_NONE, Gst.MessageType.EOS)

pipeline.set_state(Gst.State.NULL)