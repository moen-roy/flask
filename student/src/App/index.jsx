import {BrowserRouter,Routes,Route } from "react-router-dom"
import Login from "./screen/Login"
import MainDashBoard from './screen/Dashboard'
import SudentAnalytics from './screen/Dashboard/Analytics'
import AddStudent from './screen/Dashboard/Add'
import ListStudent from './screen/Dashboard/Student'
function App(){
    return <BrowserRouter>
    <Routes>
        <Route path="" element={<Login />} />
        {/*nested*/}
        <Route path="/student" element={<MainDashBoard />}>
            <Route path="" element={<SudentAnalytics />} />
            <Route path="add" element={<AddStudent/>} /> 
            <Route path="list" element={<ListStudent />} />
        </Route>
    </Routes>
    </BrowserRouter>
}
export default App;