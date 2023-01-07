import { useContext } from "react";
import { TasksContext } from "../contexts/TasksProvider";

const useTasks = () => {
  return useContext(TasksContext);
};

export default useTasks;
