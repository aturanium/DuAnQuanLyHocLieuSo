import { Text, View } from "react-native";
import MyStyles from "../../styles/MyStyles";
import { NavigationContainer } from "@react-navigation/native";
import Chat from "./Chat";
import Forum from "./Forum";
import Assist from "./Assist";
import { createMaterialTopTabNavigator } from "@react-navigation/material-top-tabs";

const Tab = createMaterialTopTabNavigator()

const Discuss = () => {
        return(
            <Tab.Navigator style={[MyStyles.marginTop, MyStyles.margin]}>
                <Tab.Screen name="Chat" component={Chat} options={{title: "Chat"}}/>
                <Tab.Screen name="Forum" component={Forum} options={{title: "Diễn đàn"}}/>
                <Tab.Screen name="Assist" component={Assist} options={{title: "Hỗ trợ"}}/>
            </Tab.Navigator>
        );
}

export default Discuss;