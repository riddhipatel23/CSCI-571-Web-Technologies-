import { useState, useEffect } from 'react';
import { loadModules } from 'esri-loader';

const Campus = (props) => {

    const [graphic, setGraphic] = useState(null);
    useEffect(() => {

        loadModules(['esri/Graphic']).then(([Graphic]) => {
            // Create a polygon geometry
            const polygon = {
                type: "polygon", // autocasts as new Polygon()
                rings: [
                    [-118.289237,34.021664],
                    [-118.286228,34.023695],
                    [-118.285365, 34.023368],
                    [-118.285063, 34.023183],
                    [-118.284648,34.018966],
                    [-118.285476,34.018582],
                    [-118.289198,34.019435],
                    [-118.289237,34.021664 ]
                ]
            };

            // Create a symbol for rendering the graphic
            const fillSymbol = {
                type: "simple-fill", // autocasts as new SimpleFillSymbol()
                color: [200,0,20, 0.25],
                outline: { // autocasts as new SimpleLineSymbol()
                    color: [255, 255, 255],
                    width: 1
                }
            };

            // Add the geometry and symbol to a new graphic
            const graphic = new Graphic({
                geometry: polygon,
                symbol: fillSymbol
            });
            setGraphic(graphic);
            props.view.graphics.add(graphic);
        }).catch((err) => console.error(err));

        return function cleanup() {
            props.view.graphics.remove(graphic);
        };
    }, []);

    return null;

}

export default Campus;