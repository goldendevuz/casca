class EventBus:
    subscribers = []

    @classmethod
    def publish(cls, event):
        for sub in cls.subscribers:
            sub(event)
