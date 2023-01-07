import React, { createContext, useState } from "react";

const TasksState = () => {
  const [doneTasks, setDoneTasks] = useState([]);
  const [undoneTasks, setUndoneTasks] = useState([]);

  return { doneTasks, setDoneTasks, undoneTasks, setUndoneTasks };
};

export const TasksContext = createContext();

const TasksProvider = ({ children }) => {
  const contextData = TasksState();
  return (
    <TasksContext.Provider value={contextData}>
      {children}
    </TasksContext.Provider>
  );
};

export default TasksProvider;
