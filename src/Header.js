// This Program is for the header, appearing in every page
//Author Name: Jaishana Bindhu Priya
//Last Modified:

//========= Headers
import React from "react"; //reactjs components
import "./Header.css"; //styling header page
// to route to different page from nav bar
import { GiHamburgerMenu } from "react-icons/gi"; //hamburger icon when on mobile dimensions
//=========End Headers

function Header() {
  // This code uses the `useLocation` hook from React Router to get the current location object, which contains information about the current URL.


  return (
    <div>
      <header className="App-header">
        
         
        <nav>
          {/* =====================Navbar ========================= */}
          <div className="navbarmain">
            
            <GiHamburgerMenu className="hamburger" />
            <ul className="navbarmain-elements"> 
              <li>
                {/*} This code is using the 'Link' component from the 'react-router-dom' library to create a clickable link that navigates to the specified URL. */}
                {/* <Link
                  to="/"
                  className={location.pathname === "/" ? "active" : ""}
                > */}
                  HOME
                {/* </Link> */}
              </li>

              <li>
                {/* <Link
                  to=""
                  className={location.pathname === "" ? "active" : ""}
                > */}
                  TRIPS
                {/* </Link> */}
                {/* This code defines a dropdown menu component with a class name of "dropdown_menu".*/}
              
              </li>
              <li>
                {/* the main activities page */}
                {/* <Link
                  to=""
                  className={
                    location.pathname === "" ? "active" : ""
                  }
                > */}
                  LOGIN
                {/* </Link> */}
                {/*drop dowm menu of activities */}
               
              </li>


            </ul>
          </div>
          {/* ====================================================================== */}
        </nav>
      </header>
    </div>
  );
}

export default Header;