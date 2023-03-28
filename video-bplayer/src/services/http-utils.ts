// const serverUrl = 'http://localhost:5000';
const serverUrl = '';

interface HttpResponse<T> extends Response {
  parseBody?: T;
}

export async function http<T>(
  request: RequestInfo,
): Promise<T> {
  let response: HttpResponse<T> = await fetch(
    request,
  );

  if (!response.ok) {
    if (response.status === 401) {
      const originalRequest = request as Request;
      const args = {
        method: originalRequest.method,
        body: originalRequest.body,
      };
      response = await fetch(new Request(originalRequest.url, args));

      if (!response.ok) {
        throw new Error(response.statusText);
      }
    } else if (response.status !== 400) {
      const err = await response.text();
      throw new Error(err);
    }
  }

  let parsedBody = null;
  try {
    // may error if there is no body
    parsedBody = await response.json();
  } catch (ex) {
    throw new Error('Error parse json');
  }

  return parsedBody;
}

export async function get<T>(
  path: string,
): Promise<T> {
  const args: RequestInit = {
    method: 'get',
    headers: {
      'Content-Type': 'application/json',
    },
  };
  const response = await http<T>(new Request(`${serverUrl}${path}`, args));
  return response;
}

export async function post<T>(
  path: string,
  body: any,
): Promise<T> {
  const args: RequestInit = {
    method: 'post',
    body: JSON.stringify(body),
    headers: {
      'Content-Type': 'application/json',
    },
  };
  const response = await http<T>(new Request(`${serverUrl}${path}`, args));
  return response;
}

export async function postFormData<T>(
  path: string,
  formData: FormData,
): Promise<T> {
  const args: RequestInit = {
    method: 'post',
    body: formData,
    headers: {
      Accept: 'application/json',
      // 'Content-Type': 'multipart/form-data',
    },
  };

  const response: HttpResponse<T> = await fetch(new Request(`${serverUrl}${path}`, args));

  if (!response.ok) {
    if (response.status !== 400) {
      const err = await response.text();
      throw new Error(err);
    }
  }

  let parsedBody = null;
  try {
    // may error if there is no body
    parsedBody = await response.json();
  } catch (ex) {
    throw new Error('Error parse json');
  }

  return parsedBody;
}

export async function put<T>(
  path: string,
  body: any,
): Promise<T> {
  const args: RequestInit = {
    method: 'put',
    body: JSON.stringify(body),
    headers: {
      'Content-Type': 'application/json',
    },
  };
  const response = await http<T>(new Request(`${serverUrl}${path}`, args));
  return response;
}
