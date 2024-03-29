import { get, post, postFormData } from '@/services/http-utils';
import User from '@/models/User';
import Video from '@/models/Video';
import Subtitle from '@/models/Subtitle';
import LoginRequest from '@/models/LoginRequest';
import VideoDownloadRequest from '@/models/VideoDownloadRequest';
import Process from '@/models/Process';

export async function register(loginRequest: LoginRequest): Promise<User> {
  const response = await post<User>('/api/register', loginRequest);
  return response;
}

export async function login(loginRequest: LoginRequest): Promise<User> {
  const response = await post<User>('/api/login', loginRequest);
  return response;
}

export async function downloadVideo(videoDownloadRequest: VideoDownloadRequest): Promise<Video> {
  const response = await post<Video>('/api/videos/download', videoDownloadRequest);
  return response;
}

export async function uploadVideo(formData: FormData): Promise<Video> {
  const response = await postFormData<Video>('/api/videos/upload', formData);
  return response;
}

export async function uploadSimpleFile(formData: FormData): Promise<string> {
  const response = await postFormData<string>('/api/simple/upload', formData);
  return response;
}

export async function processStart(process: Process): Promise<Process> {
  const response = await post<Process>('/api/process/start', process);
  return response;
}

export async function processStatus(processId: number): Promise<Process> {
  const response = await get<Process>(`/api/process/status/${processId}`);
  return response;
}

export async function getVideos(): Promise<Video[]> {
  const response = await get<Video[]>('/api/videos');
  return response;
}

export async function getVideoById(id: number): Promise<Video> {
  const response = await get<Video>(`/api/videos/${id}`);
  return response;
}

export async function getSubtitlesByVideo(videoId: number): Promise<Subtitle[]> {
  const response = await get<Subtitle[]>(`/api/subtitles/${videoId}`);
  return response;
}
