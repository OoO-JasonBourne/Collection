import temperatureDate from '../assets/temperature.json'
import kriging from 'kriging'; // 导入 kriging 库

class KrigingData {
    generate() {
        // 准备数据，包括输入的点数据和格网的参数。
        // 解析 GeoJSON 数据以获取一个点数组
        const points = temperatureDate.features.map(feature => ({
            lon: feature.geometry.coordinates[0],
            lat: feature.geometry.coordinates[1],
            value: parseFloat(feature.properties.temperature)
        }));
        // 构建 t, x, y 数组
        const t = [], x = [], y = [];
        for (let i = 0; i < points.length; i++) {
            t.push(points[i].value);
            x.push(points[i].lon);
            y.push(points[i].lat);
        }
        // 使用 kriging.js 进行 kriging 插值，生成格网数据。
        // const krigingPoints = points.map(p => [p.lon, p.lat, p.value]);

        // 格网参数
        const cellSize = 0.01; // 格网单元大小
        const gridExtent = [120, 28, 122, 30]; // 格网范围
        const model = 'exponential', sigma2 = 0.1, alpha = 100;
        // 使用 kriging.js 进行插值
        const variogram = kriging.kriging.train(t, x, y, model, sigma2, alpha);
        const gridData = kriging.kriging.grid(
            [[
                [gridExtent[0], gridExtent[1]],
                [gridExtent[2], gridExtent[1]],
                [gridExtent[2], gridExtent[3]],
                [gridExtent[0], gridExtent[3]],
            ]], variogram, cellSize);
      
        // 使用 turf.js 绘制等值面
        const fc = gridFeatureCollection(gridData, [gridExtent[0], gridExtent[2]], [gridExtent[1], gridExtent[3]]);
        // return fc
        const collection = turf.featureCollection(fc);


        const breaks = [-30, -22, -14, -6, 2, 10, 18, 26, 34, 42, 50];
        // const breaks = [-20, -16, -12, -8, -4, 0, 4, 8, 12, 16, 20];
        const isolines = turf.isolines(collection, breaks, { zProperty: 'value' });
        const isobands = turf.isobands(collection, breaks, { zProperty: 'value' });
        return [isolines, isobands]
        //利用网格计算点集
        function gridFeatureCollection(grid, xlim, ylim) {
            var range = grid.zlim[1] - grid.zlim[0];
            var i, j, x, y, z;
            var n = grid.length;//列数
            var m = grid[0].length;//行数
            var pointArray = [];
            for (i = 0; i < n; i++)
                for (j = 0; j < m; j++) {
                    x = (i) * grid.width + grid.xlim[0];
                    y = (j) * grid.width + grid.ylim[0];
                    z = (grid[i][j] - grid.zlim[0]) / range;
                    // if (z < 0.0) z = 0.0;
                    // if (z > 1.0) z = 1.0;
                    pointArray.push(turf.point([x, y], { value: z }));
                }
            return pointArray;
        }
    }
}

export default KrigingData;