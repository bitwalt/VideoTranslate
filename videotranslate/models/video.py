from dataclasses import dataclasses
    
@dataclasses    
class Video:
    name: str
    url: str
    path: str
    is_streaming: bool
        