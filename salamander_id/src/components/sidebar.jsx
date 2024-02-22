import React from "react";
import SideBarTab from "./sidebartab";

const tabsdata = [
    { id: 1, name: "Home" },
    { id: 2, name: "Library" },
    { id: 3, name: "Import" },
    { id: 4, name: "review" },
    { id: 5, name: "Backup" },
    { id: 6, name: "Mail" },
    { id: 7, name: "About" },
];

function SideBar() {
    return <div className="sidebar">

        {tabsdata.map( tab => {
            <SideBarTab 
                key={tab.id} 
                name={tab.name} 
            />  
        })}

    </div>;
}

export default SideBar;