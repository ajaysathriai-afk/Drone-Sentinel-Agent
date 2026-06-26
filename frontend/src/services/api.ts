const API_BASE_URL =
  "http://13.234.78.158:8000";

export const searchIncidents =
  async (query: string) => {

    const response =
      await fetch(
        `${API_BASE_URL}/search/?query=${query}`
      );

    return response.json();
  };


export const fetchAlerts =
  async () => {
    const response =
      await fetch(
        `${API_BASE_URL}/alerts/`
      );

    return response.json();
  };

export const fetchIncidents =
  async () => {
    const response =
      await fetch(
        `${API_BASE_URL}/incidents/`
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
  async (question: string) => {

    const response =
      await fetch(
        `${API_BASE_URL}/investigator/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            question,
          }),
        }
      );

    return response.json();
  };




export const fetchStats = async () => {
  const response = await fetch(`${API_BASE_URL}/analytics/stats`);
  return response.json();
};
