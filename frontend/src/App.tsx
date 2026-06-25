import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";

import MainLayout from "./layouts/MainLayout";

import Dashboard from "./pages/Dashboard";
import Incidents from "./pages/Incidents";
import Investigator from "./pages/Investigator";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<MainLayout />}>
          <Route path="/" element={<Dashboard />} />
          <Route
            path="/incidents"
            element={<Incidents />}
          />
          <Route
            path="/investigator"
            element={<Investigator />}
          />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
