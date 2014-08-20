import QtQuick 1.0

Rectangle {
    width: 640
    height: 480
    Image {
        anchors.fill: parent
        source: "mtg_elements_linear.png"
        fillMode: Image.PreserveAspectFit
    }
    Text {
        id: loadtext
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 40
        anchors.horizontalCenter: parent.horizontalCenter
        color: "white"
        text: "Checking for Updates"
        font.bold: true
        font.pixelSize: 20
    }
    // AnimatedImage {
    //     anchors.left: loadtext.right
    //     anchors.verticalCenter: loadtext.verticalCenter
    //     anchors.leftMargin: 10
    //     source: "loader.gif"
    // }
}
