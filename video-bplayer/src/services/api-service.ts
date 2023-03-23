import { get, post } from '@/services/http-utils';
import User from '@/models/User';
import Video from '@/models/Video';
import Subtitle from '@/models/Subtitle';
import LoginRequest from '@/models/LoginRequest';

export async function register(loginRequest: LoginRequest): Promise<User> {
  const response = await post<User>('/api/register', loginRequest);
  return response;
}

export async function login(loginRequest: LoginRequest): Promise<User> {
  const response = await post<User>('/api/login', loginRequest);
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
