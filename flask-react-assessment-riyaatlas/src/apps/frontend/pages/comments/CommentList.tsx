import React, { useEffect, useState } from "react";
import { getTasks, deleteTask } from "../../services/commentService";
import CommentForm from "./CommentForm";
import CommentItem from "./CommentItem";

interface Task {
  id: string;
  title: string;
  description: string;
}

const CommentList: React.FC = () => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [editingTask, setEditingTask] = useState<Task | null>(null);

  const fetchTasks = async () => {
    const response = await getTasks();
    setTasks(response.data);
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  const handleDelete = async (id: string) => {
    await deleteTask(id);
    fetchTasks();
  };

  const handleEdit = (task: Task) => {
    setEditingTask(task);
  };

  return (
    <div className="p-4">
      <h2 className="text-2xl font-bold mb-4">Task Management</h2>
      <CommentForm fetchTasks={fetchTasks} editingTask={editingTask} setEditingTask={setEditingTask} />
      <div className="mt-4 space-y-3">
        {tasks.map((task) => (
          <CommentItem key={task.id} task={task} onEdit={handleEdit} onDelete={handleDelete} />
        ))}
      </div>
    </div>
  );
};

export default CommentList;

