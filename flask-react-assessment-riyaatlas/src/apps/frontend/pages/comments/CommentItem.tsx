import React from "react";

interface Task {
  id: string;
  title: string;
  description: string;
}

interface Props {
  task: Task;
  onEdit: (task: Task) => void;
  onDelete: (id: string) => void;
}

const CommentItem: React.FC<Props> = ({ task, onEdit, onDelete }) => (
  <div className="border p-3 rounded flex justify-between items-center">
    <div>
      <h3 className="font-semibold">{task.title}</h3>
      <p className="text-gray-600">{task.description}</p>
    </div>
    <div className="flex gap-2">
      <button
        onClick={() => onEdit(task)}
        className="bg-yellow-400 text-white px-3 py-1 rounded hover:bg-yellow-500"
      >
        Edit
      </button>
      <button
        onClick={() => onDelete(task.id)}
        className="bg-red-500 text-white px-3 py-1 rounded hover:bg-red-600"
      >
        Delete
      </button>
    </div>
  </div>
);

export default CommentItem;
