import useSWRV from "swrv";
import { JWT_KEY_NAME } from "./constants";

// ------------------------------ Utility Functions ------------------------------
export async function apiFetcher<T>(url: string, headers?: HeadersInit) {
  const response = await fetch(url, { headers });
  const data = (await response.json()) as T;
  return { response: response.status, data };
}

export async function apiPoster<T>(
  url: string,
  body: any,
  headers?: HeadersInit
) {
  const response = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json", ...headers },
    body: JSON.stringify(body),
  });
  const data = (await response.json()) as T;
  return { response: response.status, data };
}

export async function apiPut<T>(url: string, body: any, headers?: HeadersInit) {
  const response = await fetch(url, {
    method: "PUT",
    headers: { "Content-Type": "application/json", ...headers },
    body: JSON.stringify(body),
  });
  const data = (await response.json()) as T;
  return { response: response.status, data };
}

export async function apiDelete<T>(url: string, headers?: HeadersInit) {
  const response = await fetch(url, {
    method: "DELETE",
    headers,
  });
  const data = (await response.json()) as T;
  return { response: response.status, data };
}

// ------------------------------ Client Requests ------------------------------
export async function clientFetcher<T>(url: string) {
  const token = localStorage.getItem(JWT_KEY_NAME) || "";
  const headers = {
    authorization: token,
  };

  return apiFetcher<T>(url, headers);
}

export async function clientPoster<T>(url: string, body?: any) {
  const token = localStorage.getItem(JWT_KEY_NAME) || "";
  const headers = {
    authorization: token,
  };

  return apiPoster<T>(url, body || {}, headers);
}

export async function clientPut<T>(url: string, body: any) {
  const token = localStorage.getItem(JWT_KEY_NAME) || "";
  const headers = {
    authorization: token,
  };

  return apiPut<T>(url, body, headers);
}

export async function clientDelete<T>(url: string) {
  const token = localStorage.getItem(JWT_KEY_NAME) || "";
  const headers = {
    authorization: token,
  };

  return apiDelete<T>(url, headers);
}

// SWR
export function useApi<T>(url: string) {
  const all = useSWRV(url, (url) => clientFetcher<T>(url));
  return { ...all };
}
