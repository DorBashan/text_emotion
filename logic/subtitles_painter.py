from typing import Dict, List

from models.colored_srt_part import ColoredSrtPart
from models.srt_part import SrtPart

emotions_to_colors = {
    'happy': '#add8e6',
    'sad': '#7fffd4'
}


class SubtitlesPainter:

    @staticmethod
    def paint(parts_to_emotions: Dict[SrtPart, str]) -> List[ColoredSrtPart]:
        colored_parts = []
        for part, emotion in parts_to_emotions.items():
            color_hexa = emotions_to_colors.get(emotion.lower(), '#000000')
            colored_part = ColoredSrtPart(srt_part=part, color_hexa=color_hexa)
            colored_parts.append(colored_part)

        return colored_parts

