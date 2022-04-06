import React,{ useEffect } from 'react';
import * as ReactDOM from 'react-dom';
import { Scene,WebMap,WebScene, Map } from '@esri/react-arcgis';
import Campus from './Campus';

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

//export default App;

export default (props) => (
  useEffect(() => {
    document.title = "React App - Riddhi Patel"
  }, []),
  <Map style={{ width: '70vw', height: '90vh' }}
      //mapProperties={{ basemap: 'satellite' }}
      viewProperties={{
          center: [-118.28538,34.0205],
          zoom: 15
      }}>
      <Campus />
  </Map>
)

// export default (props) => (
//   <Scene class="full-screen-map">
//       <Campus />
//   </Scene>
// )