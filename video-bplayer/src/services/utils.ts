// const serverUrl = 'http://localhost:5000';
const serverUrl = '';

const utils = {
  getUrl(filePath: string): string {
    return `${serverUrl}/${filePath}`;
  },

  durationToString(durationSeconds: number): string {
    const hours = Math.floor(durationSeconds / 3600);
    const minutes = Math.floor((durationSeconds - (hours * 3600)) / 60);
    const seconds = durationSeconds - (hours * 3600) - (minutes * 60);

    const hoursStr = hours < 10 ? `0${hours}` : `${hours}`;
    const minutesStr = minutes < 10 ? `0${minutes}` : `${minutes}`;
    const secondsStr = seconds < 10 ? `0${seconds}` : `${seconds}`;

    return hours > 0 ? `${hoursStr}:${minutesStr}:${secondsStr}` : `${minutesStr}:${secondsStr}`;
  },

  frameToSeconds(frame: number, fps: number): number {
    return Math.round(frame / fps);
  },
};

export default utils;
