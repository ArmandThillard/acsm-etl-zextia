class LiveTimings:

    live_timings = []

    def __init__(self, live_timings):
        self.live_timings = live_timings

    def get_connected_drivers(self):
        return self.live_timings['ConnectedDrivers']
        
    def get_disconnected_drivers(self):
        return self.live_timings['DisconnectedDrivers']