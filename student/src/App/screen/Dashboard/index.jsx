import { Outlet } from "react-router-dom";
function Main_dash(){
    return(
        <div>
            <h1>Main Dash</h1>
            <Outlet/>
        </div>
    )
}
export default Main_dash;