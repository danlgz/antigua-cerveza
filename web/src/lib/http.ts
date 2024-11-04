import camelcaseKeys from "camelcase-keys";

type ResponseError = {
  code: string;
  detail: string[];
}

type MakeRequestResult<T> = {
  status: number;
  data?: T;
  error?: ResponseError;
}

export default async function makeRequest<T>(path: string, tags: string[] = []): Promise<MakeRequestResult<T>> {
  try {
    // NOTE: the current use case is a "GET" request, that's why the other methods are not consider yet
    const response = await fetch(`${process.env.API_HOST}${path}`, {
      headers: {
        'Content-Type': 'application/json',
      },
      next: { tags },
    });

    if (!response.ok) {
      const error = (await response.json()) as ResponseError | undefined;

      return {
        status: response.status,
        error,
        data: undefined,
      };
    }

    return {
      status: response.status,
      error: undefined,
      data: camelcaseKeys(await response.json(), { deep: true }) as T,
    }
  } catch (error) {
    return {
      status: 500,
      error: {
        code: 'FatalError',
        detail: [(error as Error).message],
      },
      data: undefined,
    };
  }
}
