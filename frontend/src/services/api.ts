const API_BASE_URL =
  "http://127.0.0.1:8000";

export const searchIncidents =
  async (query: string) => {

    const response =
      await fetch(
        `http://127.0.0.1:8000/search/?query=${query}`
      );

    return response.json();
  };


export const fetchAlerts =
  async () => {
    const response =
      await fetch(
        `${API_BASE_URL}/alerts`
      );

    return response.json();
  };

export const fetchIncidents =
  async () => {
    const response =
      await fetch(
        `${API_BASE_URL}/incidents`
      );

    return response.json();
  };

export const analyzeImage =
  async (file: File) => {
    const formData =
      new FormData();

    formData.append(
      "file",
      file
    );

    const response =
      await fetch(
        `${API_BASE_URL}/analyze`,
        {
          method: "POST",
          body: formData,
        }
      );

    return response.json();
  };

export const fetchZoneAnalytics = async () => {
  const response = await fetch(
    `${API_BASE_URL}/analytics/`
  );

  return response.json();
};

export const chatWithInvestigator =
  async (query: string) => {

    const response =
      await fetch(
        "http://127.0.0.1:8000/chat/",
        {
          method: "POST",
          headers: {
            "Content-Type":
              "application/json",
          },
          body: JSON.stringify({
            query,
          }),
        }
      );

    return response.json();
  };

export const fetchStats = async () => {
  const response = await fetch(`${API_BASE_URL}/analytics/stats`);
  return response.json();
};
