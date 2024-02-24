import React, {useState} from 'react';
import SideBarTab from "./sidebartab";


function SideBar() {

    const tabsdata = [
        { id: 1, name: "Home" },
        { id: 2, name: "Library" },
        { id: 3, name: "Import" },
        { id: 4, name: "review" },
        { id: 5, name: "Backup" },
        { id: 6, name: "Mail" },
        { id: 7, name: "Bénévols" },
    ];

    const [selectedTab, setSelectedTab] = useState(tabsdata[0].name);

    function handleTabClick(event) {
        const tabName = event.target.textContent;
        console.log(event.target)
    }

    return <div className="sidebar">
        {tabsdata.map( tab => 
                <SideBarTab onclick={handleTabClick}
                    key={tab.id} 
                    name={tab.name} 
                />
        )}
    </div>;
}

export default SideBar;