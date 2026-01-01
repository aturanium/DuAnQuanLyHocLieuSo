import { Text, View } from "react-native";
import MyStyles from "../../styles/MyStyles";
import Chat from "./Chat";
import Forum from "./Forum";
import Assist from "./Assist";
import { createMaterialTopTabNavigator } from "@react-navigation/material-top-tabs";
import ChatDetail from "./ChatDetail";
import { createNativeStackNavigator } from "@react-navigation/native-stack";

const Tab = createMaterialTopTabNavigator()

const Stack = createNativeStackNavigator();
const StackChat =() =>{
    return(
        <Stack.Navigator screenOptions={{headerShown: false}}>
            <Stack.Screen name="Chat" component={Chat} options={{title: "Chat"}}/>
            <Stack.Screen name="Chat Detail" component={ChatDetail}/>
        </Stack.Navigator>
    );
}

const Discuss = () => {
        return(
            <Tab.Navigator style={[MyStyles.marginTop, MyStyles.margin]}>
                <Tab.Screen name="Chat" component={StackChat} options={{title: "Chat"}}/>
                <Tab.Screen name="Forum" component={Forum} options={{title: "Diễn đàn"}}/>
                <Tab.Screen name="Assist" component={Assist} options={{title: "Hỗ trợ"}}/>
            </Tab.Navigator>
        );
}

export default Discuss;