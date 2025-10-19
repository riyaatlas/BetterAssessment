import axios from "axios";

const API_BASE_URL = "http://localhost:8080/api/comments";

export const getTasks = async () => axios.get(API_BASE_URL);
export const createTask = async (task: { title: string; description: string }) =>
  axios.post(API_BASE_URL, task);
export const updateTask = async (id: string, task: { title: string; description: string }) =>
  axios.patch(`${API_BASE_URL}/${id}`, task);
export const deleteTask = async (id: string) =>
  axios.delete(`${API_BASE_URL}/${id}`);
