interface Video {
  id: number;
  videoName: string;
  videoDescription: string;
  videoCategory: string;
  videoPreviewPath: string;
  videoFilePath: string;
  durationSeconds: number;
  fps: number;
}

export default Video;
