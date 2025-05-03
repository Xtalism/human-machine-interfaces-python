 default_reading and y <= default_reading:
            self.frameColor(self.frameLeft, 0, 255, 0)
                            
    def closeEvent(self, event):
        self.timer.stop()