import { JWT_KEY_NAME } from "./constants";

export async function apiFetcher<T>(url: string) {
  const response = await fetch(url);
  const data = (await response.json()) as T;
  return { response: response.status, data };
}

export async function apiPoster<T>(url: string, body: any) {
  const response = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  const data = (await response.json()) as T;
  return { response: response.status, data };
}

// ------------------------------ Client requests ------------------------------
export async function clientFetcher<T>(url: string) {
  const token = localStorage.getItem(JWT_KEY_NAME) || "";
  const headers = new Headers();
  headers.append("authorization", token);

  const response = await fetch(url, { headers });
  const data = (await response.json()) as T;
  return { response: response.status, data };
}

export async function clientPoster<T>(url: string, body?: any) {
  const token = localStorage.getItem(JWT_KEY_NAME) || "";
  const headers = new Headers();
  headers.append("authorization", token);

  const response = await fetch(url, {
    method: "POST",
    body: JSON.stringify(body || {}),
    headers,
  });
  const data = (await response.json()) as T;
  return { response: response.status, data };
}
