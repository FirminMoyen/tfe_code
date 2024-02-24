import React from "react";

function SideBarTab(props) {
    return <div className="sidebar-tab">
            <h2 className="sidebar-button">{props.name}</h2>
    </div>;
}

export default SideBarTab;