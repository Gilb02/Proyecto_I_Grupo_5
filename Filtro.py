import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject
import cv2

Gst.init(None)

pipeline = Gst.Pipeline()
src = Gst.ElementFactory.make("v4l2src")
videoconvert1 = Gst.ElementFactory.make("videoconvert")
edge = Gst.ElementFactory.make("edgetv")
videoconvert2 = Gst.ElementFactory.make("videoconvert")
ximagesink = Gst.ElementFactory.make("ximagesink")

