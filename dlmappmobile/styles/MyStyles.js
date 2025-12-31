import { StyleSheet } from "react-native";

export default StyleSheet.create({
    container: {
        flex: 1,
        marginTop: 8
    },
    marginTop : {
        marginTop: 25,
    },
    right: {
        marginLeft: 310
    },
    row: {
        flexDirection: 'row',
        flexWrap: 'wrap',
        marginVertical: 8
    },
    column: {
        flexDirection: 'column',
        flexWrap: 'wrap',
    },
     margin: {
        margin: 2
     },
     middle: {
        marginLeft: 180
     },
     avatar: {
        width: 165,
        height: 95,
        borderRadius: 10,
     },
     image: {
        width: 80,
        height: 80,
        borderRadius: 50,
     },
    padding: {
        padding: 5
    },
    header: {
        flexDirection: 'row',
        backgroundColor: '#055a8bff',
        padding: 12,
        borderRadius: 16,
        alignItems: 'center',  
        margin: 12,
    },
    textContainer: {
        marginLeft: 10,
        flex: 1,            
        justifyContent: 'center', 
    },
    title: {
        color: 'black',
        fontSize: 18,
        fontWeight: 'bold',
        flexWrap: 'wrap',      
    },
    context: {
        color: '#fff',
        fontSize: 10,
        flexWrap: 'wrap',      
    },
    text: {
        color: 'black',
        fontSize: 10,
        flexWrap: 'wrap',      
        fontSize: 12
    },
    thumbnail: {
        borderRadius: 14,
        backgroundColor: '#eef1f4',
        justifyContent: 'center',
        alignItems: 'center',
        overflow: 'hidden',
        position: 'relative'
    },
    portalContainer: {
        backgroundColor: "white",
        padding: 10,
        margin: 10,
        borderRadius: 16
    }
})