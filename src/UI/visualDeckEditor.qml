import Qt 4.7

Rectangle {
    width: 1000
    height: 600
    Flickable {
        anchors.fill: parent
    Flow {
        anchors.fill: parent
        anchors.margins: 4
        spacing: 10
        
        Image {
            source: "http://magiccards.info/scans/en/jou/1.jpg"
        }
        Image {
            source: "http://magiccards.info/scans/en/jou/1.jpg"
        }
        Image {
            source: "http://magiccards.info/scans/en/jou/1.jpg"
        }
        Image {
            source: "http://magiccards.info/scans/en/jou/1.jpg"
        }
        Image {
            source: "http://magiccards.info/scans/en/jou/1.jpg"
        }
    }
        }
}
