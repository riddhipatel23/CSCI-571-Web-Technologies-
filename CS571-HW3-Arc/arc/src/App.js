import React,{ useEffect } from 'react';
import * as ReactDOM from 'react-dom';
import { Scene,WebMap,WebScene } from '@esri/react-arcgis';


function App(){
  useEffect(() => {
    document.title = "React App - Riddhi Patel"
  }, [])
  ReactDOM.render(
    <div style={{ width: '100vw', height: '100vh' }}>
        <WebMap id="c3a272c7050f4429b7d1421d65c39b75" />
    </div>,
  document.getElementById('root')
);
}

export default App;
