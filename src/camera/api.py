from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, status
from fastapi.responses import StreamingResponse
import io
from threading import Condition
from picamera2 import Picamera2
from picamera2.encoders import JpegEncoder
from picamera2.outputs import FileOutput

router = APIRouter(prefix="/stream", tags=["stream"])

class StreamingOutput(io.BufferedIOBase):
    def __init__(self):
        self.frame = None
        self.condition = Condition()
        self.stopped = False  # Variable to control streaming

    def write(self, buf):
        with self.condition:
            self.frame = buf
            self.condition.notify_all()

    def stop(self):
        with self.condition:
            self.stopped = True
            self.condition.notify_all()

picam2 = Picamera2()
picam2.configure(picam2.create_video_configuration(main={"size": (640, 480)}))
output = StreamingOutput()
picam2.start_recording(JpegEncoder(), FileOutput(output))

def get_frame():
    try:
        while not output.stopped:
            with output.condition:
                output.condition.wait()
                frame = output.frame

            ret = b'--FRAME\r\n'
            ret += b'Content-Type: image/jpeg\r\n'
            ret += f'Content-Length: {len(frame)}\r\n\r\n'.encode()
            ret += frame
            ret += b'\r\n'
            yield ret
    except Exception as e:
        print("Removed Streaming Client")

@router.get('/mjpeg', response_class=StreamingResponse)
def stream():
    return StreamingResponse(
        get_frame(),
        headers={
            'Age': '0',
            'Cache-Control': 'no-cache, private',
            'Pragma': 'no-cache',
            'Content-Type': 'multipart/x-mixed-replace; boundary=FRAME'
        }
    )

@router.get('/stop')
def stop_stream():
    output.stop()
    return {"message": "Streaming stopped successfully"}
