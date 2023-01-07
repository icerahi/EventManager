import React, { useEffect, useState } from "react";
import Task from "../task/Task";
import Tasks from "../../pages/tasks/Tasks";
import "./SideBar.css";
import axios from "axios";
import { domain } from "../../.env";
import useTasks from "../../hooks/useTasks";
const SideBar = ({ handleCloseSideBar }) => {
  const {doneTasks} = useTasks()

  return (
    <aside className="">
      <div className="p-3 mb-2 border-bottom d-flex justify-center-center align-items-center sticky-top bg-white">
        <button
          className="border-2 border-dark me-2 rounded-circle p-2 fw-bolder px-3 text-center bg-dark text-white"
          onClick={handleCloseSideBar}
        >
          X
        </button>
        <h5 className="fw-bolder">Your Have Done</h5>
      </div>

      <div className="row row-cols-1 g-4 p-2">
        {doneTasks.map((task, index) => (
          <Task key={index} task={task} />
        ))}
      </div>
      {doneTasks.length ===0&& <p className="text-center text-secondary">No Task Done yet !!</p> }
    </aside>
  );
};

export default SideBar;
