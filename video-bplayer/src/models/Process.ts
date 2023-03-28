interface Process {
  id: number;
  status: number;
  videoId: number;
  dateStart: Date;
  dateEnd?: Date;
  updatedAt: Date;
  isSuccess: boolean;
  errorMessage?: string;
}

export default Process;
