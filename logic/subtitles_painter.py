from typing import Dict, List

from models.colored_srt_part import ColoredSrtPart
from models.srt_part import SrtPart


class SubtitlesPainter:

    @staticmethod
    def paint(parts_to_emotions: Dict[SrtPart, str]) -> List[ColoredSrtPart]:
        colored_parts = []
        for part, emotion in parts_to_emotions.items():
            if emotion == 'happy':
                colored_part = ColoredSrtPart(srt_part=part, color_hexa='#ffff00')
                colored_parts.append(colored_part)

        return colored_parts

