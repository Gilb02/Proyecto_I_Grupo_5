import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject
import cv2

Gst.init(None)

pipeline = Gst.Pipeline()
