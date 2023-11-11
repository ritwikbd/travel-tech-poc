# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 13:57:07 2023

@author: ritwi
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 13:50:06 2023

@author: ritwi
"""
from youtube_transcript_api import YouTubeTranscriptApi
def get_video_text(video_id):
    """Takes the Youtube ID of a video and returns the entire text from its transcript. Only works on videos with caption
    Arguments: 1 string
    Returns: 1 string"""
    text=YouTubeTranscriptApi.list_transcripts(video_id)
    video_text=[]
    for transcript in text:
        if str(transcript.language) == "English (auto-generated)":
            video_text=[{'text':"Only Auto Generated"}] #Auto Generated transcript was seen to have garbage values
            video_text.extend(transcript.fetch())
            continue
        if str(transcript.language).startswith('English'):
            video_text=transcript.fetch()
            break
    full_text = ' '.join(chunk['text'] for chunk in video_text)
    return full_text

def get_summary(text):
    summary= "Summary"
    return summary

if __name__ == "__main__":
    full_video_text=get_video_text("ySpBEvEi8r8") #Created for the video at this link: https://www.youtube.com/watch?v=ySpBEvEi8r8
    print(full_video_text)
    summary=get_summary(full_video_text)
