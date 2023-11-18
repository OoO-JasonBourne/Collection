class LST {
    // 生成模拟的 [lon, lat, temperature] 格式的数据
    generateRandomTemperatureData(count, lonRange, latRange, temperatureRange) {
        const data = [];
        
        for (let i = 0; i < count; i++) {
            const lon = Math.random() * (lonRange.max - lonRange.min) + lonRange.min;
            const lat = Math.random() * (latRange.max - latRange.min) + latRange.min;
            const temperature = Math.random() * (temperatureRange.max - temperatureRange.min) + temperatureRange.min;

            data.push({
                type: 'Feature',
                geometry: {
                    type: 'Point',
                    coordinates: [lon, lat]
                },
                properties: {
                    temperature: temperature.toFixed(2)
                }
            });
        }

        return {
            type: 'FeatureCollection',
            features: data
        };
    }
}

export default LST;
